# Implementing a Pre_ Image Classifier to classify Dog Breeds

In this project I have used an already created image classifier to identify dog breeds. The purpose of this project is improve ones python skills. 
There is no need to create a classifier as it has been already provided in this repo with the file name `classifier.py`. I have just applied my Python 
skills that I have learned so far. 

## Objectives

1. Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.
2. Correctly classify the breed of dog, for the images that are of dogs.
3. Determine which CNN model architecture (ResNet, AlexNet, or VGG16) is the best achieve the objectives 1 and 2.

## Steps to run the code

- call the time functions before the start of main code and after the main logic has been finished.
- add command line argument for '--dir': uses default ='pet_images/'
- add command line argument for '--arch': default='vgg'
- add command line argument for '--dogfile': default='dognames.txt'
- make sure files starting with '.' are ignored. check for '.' using a conditional statement.
- dictionary key and label are in the correct format and retrieves 40 key-value pairs.
  e.g:- {'Poodle_07956.jpg': ['poodle'], 'fox_squirrel_01.jpg': ['fox squirrel'] ... }
- pass 'in_arg.dir' as an argument inside check_images.py while calling the get_pet_labels function.
- append images_dir to each value before making the function call.
- classifier(images_dir+users_key, model)
- convert the output to lower case and strip any whitespaces
- append 1 to correct label, and 0 to falsely classified values, classifying Labels as dogs
- check the displayed output and see if all matches and non matches are appropriately displayed.

## Results Summary for CNN Model Architecture VGG

- Pet Image Label Dictionary has 40 key-value pairs.
Below are 10 of them:
 1 key:  German_shepherd_dog_04890.jpg  label:        german shepherd dog
 2 key:                     cat_07.jpg  label:                        cat
 3 key:            Dalmatian_04068.jpg  label:                  dalmatian
 4 key:        great_horned_owl_02.jpg  label:           great horned owl
 5 key:            Dalmatian_04037.jpg  label:                  dalmatian
 6 key:       Boston_terrier_02285.jpg  label:             boston terrier
 7 key:     Golden_retriever_05257.jpg  label:           golden retriever
 8 key:       Boston_terrier_02259.jpg  label:             boston terrier
 9 key:               Poodle_07956.jpg  label:                     poodle
10 key:                     cat_02.jpg  label:                        cat

- N Images            :  40
- N Dog Images        :  30
- N Not-Dog Images    :  10
- pct_match 87.5
- pct_correct_dogs 100.0
- pct_correct_breed 93.33333333333333
- pct_correct_notdogs 100.0

INCORRECT Dog Breed Assignment:
- Real:             great pyrenees   Classifier:                         kuvasz
- Real:                     beagle   Classifier:  walker hound, walker foxhound
