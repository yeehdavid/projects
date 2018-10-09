import os
import django
import time
from abnormal.settings import coins
from abnormal.amplitude import get_amplitude
from abnormal.person_modulus import get_person
from abnormal.settings import abnormal_threshold
from sendSignal.sendEmail import send_email
from quant_models.models import Abnormal
os.environ['DJANGO_SETTINGS_MODULE'] = 'Quant.settings'
django.setup()
keys = coins.keys()


def get_abnormal():
    while True:
        amplitudes = get_amplitude()
        time.sleep(15)
        persons = get_person()
        coin_up = 0
        coin_down = 0
        amplitude_difference_max = 0
        for k_i in keys:
            for k_j in keys:
                if k_i >= k_j:
                    continue
                amplitude_difference = amplitudes[k_i] - amplitudes[k_j]
                flag = abs(amplitude_difference) * persons[k_i][k_j]
                print(flag, amplitude_difference, persons[k_i][k_j], k_i, k_j)
                if flag > abnormal_threshold:
                    if abs(amplitude_difference) > amplitude_difference_max:
                        if amplitude_difference > 0:
                            coin_up = k_j
                            coin_down = k_i
                        else:
                            coin_up = k_i
                            coin_down = k_j
                    send_email('做多{0},做空{1}'.format(coins[coin_up], coins[coin_down]))
                    Abnormal.objects.create(coin_up=coin_up, coin_down=coin_down, amplitude=amplitude_difference,
                                            person=persons[k_i][k_j], flag=flag)
        time.sleep(300)


if __name__ == '__main__':
    get_abnormal()
