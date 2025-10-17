#!/usr/bin/env python3
"""
LikewiseLightsPeaceSince - A simple demonstration of interconnected concepts
"""

import datetime


class LikewiseLightsPeaceSince:
    """
    A class representing the concepts of Likewise, Lights, Peace, and Since
    """
    
    def __init__(self):
        self.start_date = datetime.datetime.now()
        self.lights = []
        self.peace_state = True
        
    def add_light(self, name):
        """Add a light to the collection"""
        self.lights.append({
            'name': name,
            'timestamp': datetime.datetime.now()
        })
        
    def get_lights(self):
        """Get all lights"""
        return self.lights
        
    def likewise_peace(self):
        """Return a message about peace"""
        return "Likewise, may peace be with you"
        
    def since_started(self):
        """Calculate time since the instance was created"""
        now = datetime.datetime.now()
        delta = now - self.start_date
        return f"Since started: {delta.total_seconds():.2f} seconds ago"
        
    def display_status(self):
        """Display the current status"""
        print("=" * 50)
        print("Likewise Lights Peace Since - Status")
        print("=" * 50)
        print(self.likewise_peace())
        print(self.since_started())
        print(f"Lights count: {len(self.lights)}")
        for light in self.lights:
            print(f"  - {light['name']}")
        print("=" * 50)


def main():
    """Main function demonstrating the LikewiseLightsPeaceSince class"""
    instance = LikewiseLightsPeaceSince()
    
    # Add some lights
    instance.add_light("Starlight")
    instance.add_light("Moonlight")
    instance.add_light("Sunlight")
    
    # Display status
    instance.display_status()


if __name__ == "__main__":
    main()
