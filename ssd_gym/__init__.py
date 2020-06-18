from gym.envs.registration import register

register(
    id='harverst-v0',
    entry_point='ssd_gym.envs:HarverstEnv',
)

register(
    id='cleanup-v0',
    entry_point='ssd_gym.envs:CleanUpEnv',
)