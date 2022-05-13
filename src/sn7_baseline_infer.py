import solaris as sol
import os
config_path = '../yml/sn7_baseline_infer.yml'
config = sol.utils.config.parse(config_path)
print('Config:')

for k,v in config.items():
    print('%s : %s' % (k,v))

# make infernce output dir
os.makedirs(os.path.dirname(config['inference']['output_dir']), exist_ok=True)

inferer = sol.nets.infer.Inferer(config)
inferer()
