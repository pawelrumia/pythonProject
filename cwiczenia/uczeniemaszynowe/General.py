import datetime
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn import metrics

def simulate_ride_distances():
    ride_dist = np.concatenate(
        (
            10 * np.random.random(size=370),
            10 * np.random.random(size=370),
            10 * np.random.random(size=370),
            10 * np.random.random(size=370)
        )
    )
    return ride_dist


def simulate_ride_speeds():
    ride_speeds = np.concatenate(
        (
            np.random.normal(loc=30, scale=5, size=370),
            np.random.normal(loc=30, scale=5, size=10),
            np.random.normal(loc=50, scale=10, size=310),
            np.random.normal(loc=15, scale=4, size=10),
        )
    )
    return ride_speeds


def simulate_ride_data():
    ride_dists = simulate_ride_distances()
    ride_speeds = simulate_ride_speeds()
    ride_times = ride_dists / ride_speeds
    df = pd.DataFrame(
        {
            'ride_dist': ride_dists,
            'ride_time': ride_times,
            'ride_speed': ride_speeds
        }
    )
    ride_ids = datetime.date.strftime("%Y%m%d") + df.index.astype(str)
    df['ride_id'] = ride_ids
    return df

def cluster_and_label(data, create_and_show_plot=True):
    data = StandardScaler().fit_transform(data)
    db = DBSCAN(eps=0.3, min_samples=10).fit(data)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    n_clusters_ = len(set(labels)) - (1 if -1 in labels
                                      else 0)
    n_noise_ = list(labels).count(-1)

    run_metadata = {
                'nClusters': n_clusters_,
                'nNoise': n_noise_,
                'silhouetteCoefficient': metrics.silhouette_score(data, labels),
                'labels': labels,
    }
    return run_metadata

df = simulate_ride_data()

X = df[['ride_dist', 'ride_time']]
results = cluster_and_label(X, create_and_show_plot=False)
df['label'] = results['labels']