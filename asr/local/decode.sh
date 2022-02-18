#!/bin/bash

cd $root/asr

dir=exp/chain/tdnn1n_online
data_dir=data
decode_set=test

steps/online/nnet3/decode.sh --acwt 1.0 --post-decode-acwt 10.0 \
    --scoring-opts "--min-lmwt 1" \
    --nj 1 --cmd run.pl $ivec_opt \
    $dir/graph_tgsmall data/$decode_set $dir/decoded_result || exit 1;

bash local/cer.sh --cmd "run.pl" data/$decode_set $dir/graph_tgsmall $dir/decoded_result

cp exp/chain/tdnn1n_online/decoded_result/scoring_kaldi/cer_details/per_utt ./decoded_result
cp exp/chain/tdnn1n_online/decoded_result/scoring_kaldi/cer_details/per_spk ./decoded_result

#rm -r exp/chain/decoded_result
