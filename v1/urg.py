import pyperclip
import requests
text = """
,---------.  ____     __ .-------.     .-''-.             .-'''-.     ,-----.    ,---.    ,---.    .-''-. ,---------. .---.  .---..-./`) ,---.   .--.  .-_'''-.           
\          \ \   \   /  /\  _(`)_ \  .'_ _   \           / _     \  .'  .-,  '.  |    \  /    |  .'_ _   \\          \|   |  |_ _|\ .-.')|    \  |  | '_( )_   \          
 `--.  ,---'  \  _. /  ' | (_ o._)| / ( ` )   '         (`' )/`--' / ,-.|  \ _ \ |  ,  \/  ,  | / ( ` )   '`--.  ,---'|   |  ( ' )/ `-' \|  ,  \ |  ||(_ o _)|  '         
    |   \      _( )_ .'  |  (_,_) /. (_ o _)  |        (_ o _).   ;  \  '_ /  | :|  |\_   /|  |. (_ o _)  |   |   \   |   '-(_{;}_)`-'`"`|  |\_ \|  |. (_,_)/___|         
    :_ _:  ___(_ o _)'   |   '-.-' |  (_,_)___|         (_,_). '. |  _`,/ \ _/  ||  _( )_/ |  ||  (_,_)___|   :_ _:   |      (_,_) .---. |  _( )_\  ||  |  .-----.        
    (_I_) |   |(_,_)'    |   |     '  \   .---.        .---.  \  :: (  '\_/ \   ;| (_ o _) |  |'  \   .---.   (_I_)   | _ _--.   | |   | | (_ o _)  |'  \  '-   .'        
   (_(=)_)|   `-'  /     |   |      \  `-'    /        \    `-'  | \ `"/  \  ) / |  (_,_)  |  | \  `-'    /  (_(=)_)  |( ' ) |   | |   | |  (_,_)\  | \  `-'`   |         
    (_I_)  \      /      /   )       \       /          \       /   '. \_/``".'  |  |      |  |  \       /    (_I_)   (_{;}_)|   | |   | |  |    |  |  \        /         
    '---'   `-..-'       `---'        `'-..-'            `-...-'      '-----'    '--'      '--'   `'-..-'     '---'   '(_,_) '---' '---' '--'    '--'   `'-...-'          
                                                                                                                                                                          
                                                    
"""


r = requests.get("https://github.com/skakwy/cece-api-documentation/blob/7ce6d50de6cfdae9d0f6fa09900e97cde5607eab/docs.json")
print(r.text)