import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ModulationPlotter:
    def __init__(self, sampleRate=1e6, duration=0.005, f_car=2e3, f_mod=320, m_mod=0.9, phase_mod=np.pi/2):
        # Parameters Initialization
        self.sampleRate = sampleRate
        self.duration = duration
        self.f_car = f_car
        self.f_mod = f_mod
        self.m_mod = m_mod
        self.phase_mod = phase_mod
        
        # Time Vector
        self.t = np.linspace(0, duration, int(sampleRate * duration), endpoint=False)
        
        # Carriers
        self.posCarrier, self.negCarrier = self._generate_carriers()
        self.posCarrier, self.negCarrier = self._generate_carriers()
        
        # Modulante
        self.modulante = self.m_mod * np.sin(2 * np.pi * self.f_mod * self.t + self.phase_mod)
        self.modulanteDisc = self._sample_modulation(self.modulante)
        
        self.modulante180 = -1.0 * self.modulante
        self.modulante180Disc = self._sample_modulation(self.modulante180)
        
        # Modulação
        _, self.stateNum = self._generate_state(self.modulanteDisc)
        _, self.state180Num = self._generate_state(self.modulante180Disc)

        _, self.stateNumOffSet = self._generate_state(self.modulanteDisc, option='offSetMethod')
        _, self.state180NumOffSet = self._generate_state(self.modulante180Disc, option='offSetMethod')

        _, self.stateNumMCU = self._generate_state(self.modulanteDisc, option='mcuMethod')
        _, self.state180NumMCU = self._generate_state(self.modulante180Disc, option='mcuMethod')
        
    def _generate_carriers(self):
        def triangularWave(t, freq, amplitude=1.0):
            period = 1 / freq
            return amplitude * (2 * np.abs(2 * ((t / period) % 1) - 1) - 1)

        posCarrier = 0.5 * triangularWave(self.t, self.f_car) + 0.5
        negCarrier = 0.5 * triangularWave(self.t, self.f_car) - 0.5
        return posCarrier, negCarrier
    
    def _findPeaksAndValleys(self, carrier):
        # Inicializa listas para picos e vales
        peaksIndex = []
        valleysIndex = []

        # Verifica se o primeiro ponto é um pico ou vale
        if carrier[0] > carrier[1]:
            peaksIndex.append(0)
        elif carrier[0] < carrier[1]:
            valleysIndex.append(0)

        # Calcula picos e vales para o restante do sinal
        peaksIndex.extend((np.where((np.diff(np.sign(np.diff(carrier)))) < 0)[0] + 1).tolist())
        valleysIndex.extend((np.where((np.diff(np.sign(np.diff(carrier)))) > 0)[0] + 1).tolist())

        # Retorna apenas inteiros
        return peaksIndex, valleysIndex
    
    def _sample_modulation(self, modulante):
        peaksIndex, valleysIndex = self._findPeaksAndValleys(self.posCarrier)
        modulanteDisc = np.zeros_like(modulante)
        last_peak_value = 0
        for i in range(len(modulante)):
            if i in peaksIndex:
                last_peak_value = modulante[i]
            elif i in valleysIndex:
                last_peak_value = modulante[i]
            modulanteDisc[i] = last_peak_value
        return modulanteDisc

    def _generate_state(self, modulante, option='default'):
        state = np.empty(len(modulante), dtype=str)
        
        if option == 'default':
            for i in range(len(modulante)):
                if modulante[i] > self.posCarrier[i]:
                    state[i] = 'P'
                elif modulante[i] < self.posCarrier[i] and modulante[i] > self.negCarrier[i]:
                    state[i] = 'Z'
                else:
                    state[i] = 'N'

        elif option == 'offSetMethod':
            for i in range(len(modulante)):
                if modulante[i] > 0:
                    
                    if modulante[i] > self.posCarrier[i]:
                        state[i] = 'P'
                    else:
                        state[i] = 'Z'

                else:
                    modulanteOffset = modulante[i] + 1
                    
                    if modulanteOffset > self.posCarrier[i]:
                        state[i] = 'Z'
                    else:
                        state[i] = 'N'

        elif option == 'mcuMethod':
            # Constante de tempo
            MODULATOR_COUNTSPERISR = int(self.sampleRate / self.f_car / 2)

            # Constantes para direção
            DIR_POS = 'P'
            DIR_NEG = 'N'
            DIR_ZERO = 'Z'

            # Encontra Picos e Vales da Portadora e ordena
            peak, valley = self._findPeaksAndValleys(self.posCarrier)
            events = sorted([(time, 'valley') for time in valley] + [(time, 'peak') for time in peak])

            # Cria uma lista para armazenar o estado
            state = []

            for time, event_type in events:

                # Encontra o valor de modulante no instante de tempo correspondente
                mod_value = modulante[time]

                # Define o maior e menor nivel de tensão que podera ser sintetizado
                higherLevel = DIR_POS if mod_value > 0 else DIR_ZERO
                lowestLevel = DIR_ZERO if mod_value > 0 else DIR_NEG
                
                # Ajusta o valor da modulante se for negativo (aplica um offset)
                if mod_value < 0:
                    mod_value = 1.0 + mod_value
                    
                # Calcula os vetores baseados na direção da portadora
                levelCMAX = higherLevel if event_type == 'valley' else lowestLevel
                levelT1 = lowestLevel if event_type == 'valley' else higherLevel

                if event_type == 'valley':
                    timeValue = int(mod_value * MODULATOR_COUNTSPERISR)
                else :
                    timeValue = int(MODULATOR_COUNTSPERISR - (mod_value * MODULATOR_COUNTSPERISR))
                
                # Inicializa o vetor com o valor de levelCMAX
                vector = [levelCMAX] * MODULATOR_COUNTSPERISR
    
                # Preenche os ultimos valores de timeValue até o final com levelT1
                vector[timeValue:] = [levelT1] * (MODULATOR_COUNTSPERISR - timeValue)

                # Adiciona o vetor criado à lista de estados
                state.extend(vector)
            
            # Converte a lista para um array NumPy
            state = np.array(state)
             
        # State Numérico            
        stateNum = np.where(state == 'P', 1, np.where(state == 'Z', 0, -1))
        
        return state, stateNum


    def plot(self):
        fig = make_subplots(rows=4, cols=1, 
                            shared_xaxes=True, 
                            row_heights=[0.7, 0.3, 0.3, 0.3], 
                            vertical_spacing=0.05)
        # Portadora
        fig.add_trace(go.Scatter(x=self.t, y=self.posCarrier, mode='lines', name='Pos Carrier'), row=1, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.negCarrier, mode='lines', name='Neg Carrier'), row=1, col=1)
        
        # Modulante
        fig.add_trace(go.Scatter(x=self.t, y=self.modulante, mode='lines', name='Sinal Modulante'), row=1, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.modulante180, mode='lines', name='Sinal Modulante 180'), row=1, col=1)
        
        # Modulante Discreta
        fig.add_trace(go.Scatter(x=self.t, y=self.modulanteDisc, mode='lines', name='Amostragem Sinal Modulante'), row=1, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.modulante180Disc, mode='lines', name='Amostragem Sinal Modulante 180'), row=1, col=1)

        # Estados de Modulacao Comparação com duas Portadoras
        fig.add_trace(go.Scatter(x=self.t, y=self.stateNum, mode='lines+markers', name='State', line=dict(color='red')), row=2, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.state180Num, mode='lines+markers', name='State 180', line=dict(color='green')), row=2, col=1)
        
        # Estados de Modulacao usando offSetMethod
        fig.add_trace(go.Scatter(x=self.t, y=self.stateNumOffSet, mode='lines+markers', name='State', line=dict(color='red')), row=3, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.state180NumOffSet, mode='lines+markers', name='State 180', line=dict(color='green')), row=3, col=1)

        # Estados de Modulacao usando MCU Method
        fig.add_trace(go.Scatter(x=self.t, y=self.stateNumMCU, mode='lines+markers', name='State', line=dict(color='red')), row=4, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.state180NumMCU, mode='lines+markers', name='State 180', line=dict(color='green')), row=4, col=1)
        
        fig.update_layout(
            title='Modulacao 3L',
            xaxis_title='Tempo [s]',
            yaxis_title='Amplitude',
            legend_title='Legenda',
            template='plotly',
            width=2800,
            height=800,
        )
        fig.update_yaxes(title_text="Modulation", row=1, col=1)
        fig.update_yaxes(title_text="State", tickvals=[-1, 0, 1], ticktext=['N', 'Z', 'P'], row=2, col=1)
        fig.update_yaxes(title_text="State", tickvals=[-1, 0, 1], ticktext=['N', 'Z', 'P'], row=3, col=1)
        
        return fig


plotter = ModulationPlotter(m_mod=0.6, f_car=2e3, duration=0.005, f_mod=160, phase_mod=0)
plotter.plot()
