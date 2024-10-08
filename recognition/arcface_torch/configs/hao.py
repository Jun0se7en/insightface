from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.margin_list = (1.0, 0.0, 0.4)
config.network = "r100"
config.resume = False
config.output = "/kaggle/working/"
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 1e-4
config.batch_size = 32
config.lr = 0.1
config.verbose = 2000
config.dali = False

config.rec = "/kaggle/input/splited-casia-webmaskedface/splited-CASIA-WebMaskedFace/train"
config.num_classes = 10575
config.num_image = 257326
config.num_epoch = 50
config.warmup_epoch = 0
config.val_targets = ['lfw', 'cfp_fp', "agedb_30"]
