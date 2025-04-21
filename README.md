# kafka-streaming-project

A comprehensive exploration of Apache Kafka producers and consumers using the Confluent Kafka client library, tested with various configurations and failure scenarios.

*Kindly note that this isn't a production-grade project, but a PET PROJECT*

## Project Overview

This project implements:
- A Kafka producer application sending events to 2 topics
- A consumer group with 3 instances consuming messages
- Various configuration tests for both producers and consumers
- Failure scenario simulations

## Architecture
<img width="762" alt="ARCHITECTURE" src="https://github.com/user-attachments/assets/20c4e3f1-e38a-4b61-8cac-5e4a33fce022" />


## Technical Stack

- **Kafka Client**: Confluent Kafka library
- **Environment**: Docker Compose using Confluent's containers
- **Language**: Python

## Producer Implementation

### Key Features
- Configurable acknowledgment modes (`acks=0`, `acks=1`, `acks=all`)
- Delivery report callback implementation
- Multiple partition strategies tested
- Explicit message flushing behavior analysis

### Configuration Tests
| Configuration | Behavior Observed |
|--------------|-------------------|
| `acks=0` | Fire-and-forget, highest throughput but no delivery guarantees |
| `acks=1` | Leader acknowledgment, moderate reliability |
| `acks=all` | Full ISR acknowledgment, highest reliability |
| `callback` + `flush()` | Ensures delivery reports for all messages |
| `callback` without `flush()` | Delivery reports may be missed for buffered messages |

### Key Findings
- `flush()` is essential for delivery guarantees in synchronous workflows
- `poll()` is required to trigger delivery reports even when not consuming
- Partition strategies significantly affect message distribution

## Consumer Implementation

### Setup
- Consumer group with 3 instances
- Multiple partition assignment strategies tested

### Tested Scenarios
1. **Group Rebalancing**:
   - Dynamic addition/removal of consumers
   - Consumer failure simulation
   - Processing during rebalance events

2. **Configuration Tests**:
   - `auto.offset.reset` (earliest vs latest)
   - `enable.auto.commit` (true/false)
   - `isolation.level` (read_committed)
   - `max.poll.interval.ms` adjustments

### Key Findings
- Consumer group coordination overhead during rebalances
- Importance of proper offset management for exactly-once processing
- Tradeoffs between automatic and manual offset commits

## Getting Started

### Prerequisites
- Docker and [Docker Compose](https://github.com/confluentinc/cp-all-in-one/blob/7.9.0-post/cp-all-in-one/docker-compose.yml)

### Installation
1. Clone this repository
2. Start Kafka environment:
   ```bash
   docker-compose up -d
