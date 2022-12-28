_base_=['./centerpoint_decision_tracker_BASE_dd_td.py']

model=dict(
        net=dict(
            type='TrackingModules',
            #feature extractors
            bev_attn=dict(),
            MLP_encode_BEV1=dict(),
            MLP_encode_BEV2=dict(),
            MLP_encode_motion=dict(), 
            #transformer
            EncoderNorm=dict(),
            DecoderNorm=dict(),
            TransformerEncoderLayer=dict(),
            TransformerDecoderLayer=dict(),
            TransformerEncoder=dict(),
            TransformerDecoder=dict(),
            pad=dict(),
            #decisions
            MLPMerge=dict(),
            MLPMatch=dict(),
            MLPDetNewborn=dict(),
            MLPDetFalsePositive=dict(),
            MLPTrackFalsePositive=dict(),
            MLPTrackFalseNegative=dict(),
            #pretext
            MLPRefine=dict(),
            MLPPredict=dict(),
            MLPProjPredict=dict(),
            #lstm
            lstm=dict(),
            h0=dict(),
            c0=dict(),
            #pooling 
            decision_pooling=dict(),
            self_loop_pooling=dict(),
            #lstms
            false_negative_emb=dict(),
            decisions=dict(),
            #bev
            bev_pos_enc=dict(),
            bev_EncoderNorm=dict(),
            bev_TransformerEncoderLayer=dict(),
            bev_TransformerEncoder=dict(),
            bev_forecast_proj=dict(),
            bev_confidence_proj=dict(),
            #embs
            class_embeddings=dict(),
            #EdgeGNN,
            decision_edge_linear=dict(),
            edge_gnn=dict(),
        )
    )