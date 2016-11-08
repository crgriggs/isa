combine.py takes one argument that specifies the folder where the instructions are modeled. For example cs_selector folder has models for instructions that only model the effects instructions have on the cs_selector. header.txt just has the overall model information, state.txt has the state module, and control has the control/execution part.

For example

python combine.py cs_selector

will generate a state.ucl file that then can be run with uclid