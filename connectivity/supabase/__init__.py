import os
from supabase import Client, create_client

SUPABASE_URL=os.getenv('SUPABASE_URL')
SUPABASE_KEY=os.getenv('SUPABASE_KEY')
PROBE_ID=os.getenv('PROBE_ID')

if SUPABASE_URL is None or SUPABASE_KEY is None or PROBE_ID is None:
    raise Exception('Missing env variables')

supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def set_probe_as_running() -> None:
    global supabase_client
    
    supabase_client.table("probes").update({ "status": "RUNNING" }).eq("id", PROBE_ID).execute()
