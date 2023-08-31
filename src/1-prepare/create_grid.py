import os
import shutil

debug = False


if debug:
    path_bot = os.path.join('..','..','data','1-external','vzm-j19_6-v1a_20m.bot')
    path_fxw = os.path.join('..','..','data','1-external','vzm-j19_6-v1a_20m.fxw')
    output_bot = os.path.join('..','..','data','3-input','vzm-j19_6-v1a_20m.bot')
    output_fxw = os.path.join('..','..','data','3-input','vzm-j19_6-v1a_20m.fxw')
else: 
    path_bot = snakemake.input.path_bot
    path_fxw = snakemake.input.path_fxw
    output_bot = snakemake.output.output_bot
    output_fxw = snakemake.output.output_fxw

print('copy from:')
print(path_bot)
print('copy to:')
print(output_bot)

## In this demo only files are copied, but in reality bed and fxw are created based on external data.

shutil.copyfile(path_bot, output_bot)
shutil.copyfile(path_fxw, output_fxw)