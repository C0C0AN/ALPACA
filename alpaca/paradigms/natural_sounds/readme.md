## Natural sounds experiment

This script is written to replicate the stimulation protocol described in:
- Santoro R, Moerel M, De Martino F, Valente G, Ugurbil K, Yacoub E, Formisano E (2017) Reconstructing the spectrotemporal modulations of real-life sounds from fMRI response patterns. Proceedings of the National Academy of Sciences of the United States of America 114(18): 4799–4804. <https://doi.org/10.1073/pnas.1617622114>

### Stimuli preparation

1. Download the sound files from the authors'  [repository under title _DesignProtocolsStimuli_Experiment2_](https://doi.org/10.5061/dryad.np4hs).

2. Unzip the downloaded zip file.

3. Copy all the sound files inside `Experiment2_Sounds` folder to `/path/to/alpaca/natural_sounds_experiment/stimuli` folder.

4. Confirm that the experiment script is working.
    - In Psychopy standalone, by opening `/path/to/alpaca/scripts_stimulation/natural_sounds_experiment/exp_natural_sounds.py` in [Psychopy](http://www.psychopy.org/) and clicking on `run` button.
    - If you are using psychopy as a python module (e.g. in a virtual python environment), you can do:
    ```
    cd /path/to/alpaca/scripts_stimulation/natural_sounds_experiment/
    python exp_natural_sounds.py
    ```
