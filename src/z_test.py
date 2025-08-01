import os
import importlib
import piper_phonemize

espeak_lib_path = piper_phonemize.__file__
espeak_dict_path= os.path.join(
    os.path.dirname(espeak_lib_path),
    'share', 'espeak-ng-data'
)

# init espeak backend on the first call
# if espeak_dict_path has any update, reinit piper_phonemize
print ('-'*80)
print ('org')
phoneset = piper_phonemize.phonemize_espeak(text='fred', voice='ro', data_path=espeak_dict_path)
print (phoneset)
phoneset = piper_phonemize.phonemize_espeak(text='apple', voice='ro', data_path=espeak_dict_path)
print (phoneset)

### once dict res has changed
print ()
print ('-'*80)
print ('dict_res changeed')
if not os.path.exists(f'{espeak_dict_path}/ro_dict.old'):
    os.system(f'cp {espeak_dict_path}/ro_dict {espeak_dict_path}/ro_dict.old')
os.system(f'cp src/ro_dict {espeak_dict_path}')
new_path = espeak_dict_path
espeak_dict_path = new_path
importlib.reload(piper_phonemize)
phoneset = piper_phonemize.phonemize_espeak(text='fred', voice='ro', data_path=espeak_dict_path)
print (phoneset)
phoneset = piper_phonemize.phonemize_espeak(text='apple', voice='ro', data_path=espeak_dict_path)
print (phoneset)