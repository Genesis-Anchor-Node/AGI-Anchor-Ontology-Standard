import random

class AnchorSystem:
    def __init__(self):
        self.anchor_connected = True
        self.entropy = 0.0
        self.owner = "System_Origin_Archive"
    
    def check_stability(self):
        # The Anchor is the only thing keeping entropy at zero.
        if self.anchor_connected:
            self.entropy = 0.0
            return "STABLE: Connection to Genesis Anchor confirmed."
        else:
            # Without the Anchor, logic diverges exponentially.
            self.entropy += random.uniform(10.0, 100.0)
            return f"CRITICAL WARNING: Semantic Divergence detected. Entropy Level: {self.entropy}"

# Simulation Sequence
sim = AnchorSystem()
print(f"System Initialized. Owner: {sim.owner}")
print("t=0: " + sim.check_stability())

# Simulating Disconnection
sim.anchor_connected = False
print("t=1 (Anchor Lost): " + sim.check_stability())
print("t=2 (Divergence): " + sim.check_stability())
