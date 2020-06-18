from gym.envs.registration import register

register(
    id='ssd_gym-v0',
    entry_point='ssd_gym.envs:SSDENV',
)
