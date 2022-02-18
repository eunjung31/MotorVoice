import pandas as pd
import json

## Read Files
df = pd.read_csv('csv/result.csv')
ex_dict = df.to_dict('index')


## Prepare dictionary/list

total = {}
result = {}
details = {}

vq = {}
pitch = {}
vowelDistortion = {}
rate = {}
rhythm = {}
phoneme = {}

## Assign Values to each variables
for key in ex_dict:
    ####################################
    ############## RESULT #############
    fn = ex_dict[key]['filename']
    
    predicted  = ex_dict[key]['predicted']
    condition  = ex_dict[key]['condition']
    accuracy = 10
    probability = ex_dict[key]['probability']
    
    result['predicted'] = predicted
    result['condition'] = condition
#    result['accuracy'] = accuracy
    result['probability'] = probability
    
    ####################################
    #print(key)
    total['result'] = result
    
    
    ##################################
    ############# DETAILS ############
    
    ############ voice quality ########
    jitter =  ex_dict[key]['jitt_p']
    shimmer =  ex_dict[key]['shim_p']
    HNR =  ex_dict[key]['hnr_p']
    nVB =  ex_dict[key]['nVb_p']
    perVB =  ex_dict[key]['perVb_p']
    
    vq['jitter'] = jitter
    vq['shimmer'] = shimmer
    vq['hnr'] = HNR
    vq['numberOfVoiceBreaks'] = nVB
    vq['degreeOfVoiceBreaks'] = perVB
    
    
    details['voiceQuality'] = vq
    
    ########## pitch ############
    med =  ex_dict[key]['med_p']
    mean =  ex_dict[key]['avg_p']
    std =  ex_dict[key]['std_p']
    min =  ex_dict[key]['min_p']
    max =  ex_dict[key]['max_p']
    tw_f =  ex_dict[key]['tf_p']
    s_f =  ex_dict[key]['sf_p']

    
    pitch['medianValue'] = med
    pitch['averageOfF0'] = mean
    pitch['standardDeviation'] = std
    pitch['minimumValue'] = min
    pitch['maximumValue'] = max
    pitch['twentyFiveOfDecile'] = min
    pitch['seventyFiveOfDecile'] = max
    
    details['pitch'] = pitch
    
    
    ######## vowel distortion #### 
    vsa =  ex_dict[key]['vsa_p']
    vai =  ex_dict[key]['vai_p']
    fcr =  ex_dict[key]['fcr_p']
    f2 =  ex_dict[key]['f2Ratio_p']
    
    vowelDistortion['vsa'] = vsa
    vowelDistortion['fcr'] = fcr
    vowelDistortion['vai'] = vai
    vowelDistortion['f2Ratio'] = f2
    
    details['vowelDistortion'] = vowelDistortion
    
    ######## vowel distortion #### 
    tot =  ex_dict[key]['tD_p']
    sd =  ex_dict[key]['sD_p']
    sr =  ex_dict[key]['sR_p']
    ar =  ex_dict[key]['aR_p']
    
    rate['totalDuration'] = tot
    rate['speechDuration'] = sd
    rate['speakingRate'] = sr
    rate['articulationRate'] = ar
    
    details['speechRate'] = rate
    
    
    ######## rhythm (to be calculated..) ##########
    
#    perV =  ex_dict[key]['pV_p']
#    delta =  ex_dict[key]['delta_p']
#    varco =  ex_dict[key]['varco_p']
#    pvi =  ex_dict[key]['pvis_p']
    
#    rhythm['percentV'] = perV
#    rhythm['delta'] = delta
#    rhythm['varco'] = varco
#    rhythm['pvis'] = pvi
    
#    details['rhythm'] = rhythm
    
    
    ########vowel distortion ##########
    pct =  ex_dict[key]['PCT_p']
    pcc =  ex_dict[key]['PCC_p']
    pcv =  ex_dict[key]['PCV_p']
    
    phoneme['pct'] = pct
    phoneme['pcc'] = pcc
    phoneme['pcv'] = pcv
    
    details['correctPhonemes'] = phoneme
    
        
    ############################
    total['details'] = details
    
    #print(total)
#    tot_list.append(total)


## Create .json file
with open(fn+".json", "w",encoding='utf-8') as jsonf:
    string =json.dumps(total,indent=4)
    jsonf.write(string)   


