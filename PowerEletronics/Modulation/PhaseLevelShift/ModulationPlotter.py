import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ModulationPlotter:
    def __init__(self, sampleRate=1000e3, duration=0.005, f_car=3e3, f_mod=320, m_mod=0.9, phase_mod=np.pi/2):
        self.sampleRate = sampleRate
        self.duration = duration
        self.f_car = f_car
        self.f_mod = f_mod
        self.m_mod = m_mod
        self.phase_mod = phase_mod
        self.t = np.linspace(0, duration, int(sampleRate * duration), endpoint=False)
        self.modulante = self.m_mod * np.sin(2 * np.pi * self.f_mod * self.t + self.phase_mod)
        self.posCarrier, self.negCarrier = self._generate_carriers()
        self.modulanteDisc = self._sample_modulation()
        self.state, self.stateNum = self._generate_state()

    def _generate_carriers(self):
        def triangularWave(t, freq, amplitude=1.0):
            period = 1 / freq
            return amplitude * (2 * np.abs(2 * ((t / period) % 1) - 1) - 1)

        posCarrier = 0.5 * triangularWave(self.t, self.f_car) + 0.5
        negCarrier = 0.5 * triangularWave(self.t, self.f_car) - 0.5
        return posCarrier, negCarrier

    def _sample_modulation(self):
        peaksIndex = np.where((np.diff(np.sign(np.diff(self.posCarrier))) < 0))[0] + 1
        valleysIndex = np.where((np.diff(np.sign(np.diff(self.negCarrier))) > 0))[0] + 1
        modulanteDisc = np.zeros_like(self.modulante)
        last_peak_value = 0
        for i in range(len(self.modulante)):
            if i in peaksIndex:
                last_peak_value = self.modulante[i]
            elif i in valleysIndex:
                last_peak_value = self.modulante[i]
            modulanteDisc[i] = last_peak_value
        return modulanteDisc

    def _generate_state(self):
        state = np.empty(len(self.modulanteDisc), dtype=str)
        for i in range(len(self.modulanteDisc)):
            if self.modulanteDisc[i] > self.posCarrier[i]:
                state[i] = 'P'
            elif self.modulanteDisc[i] < self.posCarrier[i] and self.modulanteDisc[i] > self.negCarrier[i]:
                state[i] = 'Z'
            else:
                state[i] = 'N'
        stateNum = np.where(state == 'P', 1, np.where(state == 'Z', 0, -1))
        return state, stateNum

   #def _mcu_implementation(self):


    def plot(self):
        fig = make_subplots(rows=2, cols=1, 
                            shared_xaxes=True, 
                            row_heights=[0.7, 0.3], 
                            vertical_spacing=0.05)
        fig.add_trace(go.Scatter(x=self.t, y=self.modulante, mode='lines', name='Sinal Modulante'), row=1, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.modulanteDisc, mode='lines', name='Amostragem nos Picos e Vales'), row=1, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.posCarrier, mode='lines', name='Pos Carrier', line=dict(color='orange')), row=1, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.negCarrier, mode='lines', name='Neg Carrier', line=dict(color='green')), row=1, col=1)
        fig.add_trace(go.Scatter(x=self.t, y=self.stateNum, mode='lines+markers', name='State', line=dict(color='red')), row=2, col=1)
        
        fig.update_layout(
            title='Modulacao 3L',
            xaxis_title='Tempo [s]',
            yaxis_title='Amplitude',
            legend_title='Legenda',
            template='plotly',
            width=3200,
            height=800,
        )
        fig.update_yaxes(title_text="Modulation", row=1, col=1)
        fig.update_yaxes(title_text="State", tickvals=[-1, 0, 1], ticktext=['N', 'Z', 'P'], row=2, col=1)
        
        return fig
