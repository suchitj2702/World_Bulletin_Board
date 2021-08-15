CREATE TABLE users (
    id BIGSERIAL,
    username VARCHAR(30) UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);

CREATE TABLE posts (
    id BIGSERIAL,
    author_id BIGINT NOT NULL,
    title VARCHAR(255),
    body TEXT,
    img_url TEXT,
    longitude REAL NOT NULL,
    latitude REAL NOT NULL,
    tags TEXT ARRAY,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users (id)
        ON DELETE CASCADE
);
