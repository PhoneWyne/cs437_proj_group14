import solaris as sol
import os
config_path = '../yml/sn7_baseline_train.yml'
config = sol.utils.config.parse(config_path)
print('Config:')


for k,v in config.items():
    print('%s : %s' % (k,v))


# make model output dir
os.makedirs(os.path.dirname(config['training']['model_dest_path']), exist_ok=True)

trainer = sol.nets.train.Trainer(config=config)
trainer.train()
