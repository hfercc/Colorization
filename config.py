import os, sys

path = os.path.split(__file__)[0]
# print("abs path is %s" %(os.path.abspath()))

config = {
    'arch': 'ResNet',
    'batch_size' : 8,
    'val_batch_size':1,
    'num_iters':1000000000,
    'seed' : 1,
    'lr':3.16e-4,

    'lr_update_step':37500,
    'test_cycle':1,

    'cuda' : True,
    'gpus' :1,
    'gpuargs' : {'num_workers': 4, 
               'pin_memory' : True
              },

    'model':'ColorizationResNet',
    'bachnorm':True,
    'pretrained':False,

    # 'opt_config':{
    #     'lr' : 0.001,
    #     'betas' : (0.9, 0.99),
    #     'eps': 1e-8,
    #     'weight_decay': 0.004
    # },

    'save' :'%s/work_cub/' % path,

    'image_folder_train' : {
        'root' : '%s/' % path,
        'file' : '/data/CUB_200_2011/*/*/*.jpg',
        'replicates': 1,
        'train':True
    },
    'image_folder_val' : {
        'root' : '%s/' % path,
        'file' : '/data/CUB_200_2011/val/*/*.jpg',
        'replicates': 1,
        'train':False
    },

    'log_frequency': 1, #frequency for the number of epotch
    'save_iamge':'%s/work/img/' % path
}

# print(config['save'])
