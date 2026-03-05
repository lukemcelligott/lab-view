import docker

client = docker.from_env()

def get_containers_info() {
    containers = client.containers.list()
    container_info = []
    for c in containers:
        container_info.append({
            "name": c.name,
            "status": c.status,
            "image": c.image.tags[0] if c.image.tags else "N/A",
            "uptime": c.attrs['State']['StartedAt']
        })
    return container_info
}
