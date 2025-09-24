def get_prediction(model, image):
    results = model(image)
    probs = results[0].probs  # Probs object
    
    # Get the index of the top1 predicted class
    pred_index = probs.top1
    
    # Get confidence score for top1 prediction
    pred_confidence = probs.top1conf.item()
    
    # Get class name from model.names dictionary (index -> class name)
    pred_class = results[0].names[pred_index]
    
    return pred_class, pred_confidence
