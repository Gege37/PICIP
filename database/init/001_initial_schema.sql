-- =====================================
-- PICIP DATABASE FOUNDATION
-- Version 1.1
-- Phase 5 Intelligence Schema
-- =====================================


CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    username VARCHAR(100) UNIQUE NOT NULL,

    email VARCHAR(255),

    role VARCHAR(50) DEFAULT 'operator',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE media_sources (

    id SERIAL PRIMARY KEY,

    name VARCHAR(255) NOT NULL,

    type VARCHAR(50),

    url TEXT,

    country VARCHAR(100),

    active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE articles (

    id SERIAL PRIMARY KEY,

    source_id INTEGER REFERENCES media_sources(id),

    title TEXT NOT NULL,

    content TEXT,

    url TEXT,

    language VARCHAR(20),

    published_at TIMESTAMP,

    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE ai_analysis (

    id SERIAL PRIMARY KEY,

    article_id INTEGER REFERENCES articles(id),

    summary TEXT,

    sentiment VARCHAR(20),

    sentiment_score DECIMAL(5,2),

    category VARCHAR(100),

    impact VARCHAR(30),

    topics TEXT,


    engine VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE alerts (

    id SERIAL PRIMARY KEY,

    article_id INTEGER REFERENCES articles(id),

    alert_level INTEGER,

    alert_type VARCHAR(30),

    message TEXT,

    email_sent BOOLEAN DEFAULT FALSE,

    whatsapp_sent BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE reports (

    id SERIAL PRIMARY KEY,

    report_type VARCHAR(50),

    content TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE system_logs (

    id SERIAL PRIMARY KEY,

    service VARCHAR(100),

    message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
