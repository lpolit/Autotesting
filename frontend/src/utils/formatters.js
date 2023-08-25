export function capitalize(word){
    return word.charAt(0).toUpperCase() + word.slice(1);
}

export function replace_description(origin, value, index){
    if (value !== "")
        origin = origin.replace("{"+index+"}", value);
    return origin;
};