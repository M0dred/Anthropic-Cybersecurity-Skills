# API Reference - Responding To Malicious Kubernetes Pods

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Kubernetes
kubectl get pods -A -o wide
kubectl describe pod suspicious-pod -n default
kubectl delete pod suspicious-pod -n default --grace-period=0
kubectl cordon node-01
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |