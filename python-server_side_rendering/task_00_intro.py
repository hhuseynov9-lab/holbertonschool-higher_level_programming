import os

def generate_invitations(template, attendees):
    # Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries, got {type(attendees).__name__}.")
        return

    # Boş girişlərin yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholder siyahısı
        for key in ["name", "event_title", "event_date", "event_location"]:
            # Məlumat yoxdursa və ya None-dırsa "N/A" ilə əvəz et
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Placeholder-i dəyişdir
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # Faylın adını təyin et
        file_name = f"output_{i}.txt"
        
        # Əgər eyni fayl varsa, os.path.exists ilə yoxlamaq olar, amma tapşırıq sadəcə yazmağı tələb edir
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"An error occurred while writing to {file_name}: {e}")
