# Project Plan to Achieve Advanced Level for Task 7.2HD  
## Healthcare Appointment Booking System  
**Timeline**: 26/05/2025 - 31/05/2025  
**Objective**: Complete all remaining tasks to achieve **Advanced** level in Project Work and ULO Achievement for Task 7.2HD, ensuring a high-quality presentation and demonstration.

---

## Day 1: 26/05/2025 (Today, Starting 3:30 PM AEST)  
**Focus**: Frontend Development and Backend API Setup  
**Total Time**: ~4 hours (3:30 PM - 7:30 PM)

### Tasks  
1. **Enhance Flask Frontend with HTML/CSS** (1.5 hours, 3:30 PM - 5:00 PM)  
   - Create a user-friendly booking interface using HTML/CSS templates.  
   - Add a form to `/book` route for users to select a doctor and appointment time.  
   - Update `app.py` to render the HTML template.  
   - Test the interface on `localhost:5000/book`.  
   - Take a screenshot: `flask_booking_form.png`.  

2. **Develop Backend API Endpoints** (2.5 hours, 5:00 PM - 7:30 PM)  
   - Implement two API endpoints in Flask:  
     - `POST /book-appointment`: Save appointment data (patient_name, doctor_id, appointment_time) to PostgreSQL.  
     - `GET /appointments`: Retrieve all appointments from the `appointments` table.  
   - Use `psycopg2` to connect Flask to PostgreSQL (container `postgres`, database `healthcare`).  
   - Test endpoints using Postman or `curl`.  
   - Take screenshots: `api_post.png` (POST response), `api_get.png` (GET response).  

**Deliverables**  
- Updated `app.py` with new routes and database integration.  
- HTML/CSS files: `templates/book.html`, `static/style.css`.  
- Screenshots: `flask_booking_form.png`, `api_post.png`, `api_get.png`.  

---

## Day 2: 27/05/2025  
**Focus**: Containerization and Kubernetes Deployment for Flask  
**Total Time**: ~5 hours (9:00 AM - 2:00 PM)

### Tasks  
1. **Create Dockerfile for Flask App** (1 hour, 9:00 AM - 10:00 AM)  
   - Write a `Dockerfile` for the Flask app:  
     - Base image: `python:3.9-slim`.  
     - Install dependencies: `flask`, `psycopg2-binary`.  
     - Copy `app.py`, `templates/`, `static/`.  
     - Expose port 5000.  
   - Build and test the container locally:  
     ```bash  
     docker build -t flask-app:latest .  
     docker run -p 5000:5000 flask-app:latest  
     ```  
   - Verify the app runs at `localhost:5000`.  

2. **Deploy Flask App to Kubernetes** (2 hours, 10:00 AM - 12:00 PM)  
   - Push the Flask image to Docker Hub (or use a local registry).  
   - Create Kubernetes YAML files:  
     - `flask-deployment.yaml`: Deployment with 2 replicas, image `flask-app:latest`, port 5000.  
     - `flask-service.yaml`: ClusterIP Service to expose Flask app on port 5000.  
   - Apply the configurations:  
     ```bash  
     kubectl apply -f flask-deployment.yaml  
     kubectl apply -f flask-service.yaml  
     ```  
   - Port-forward to test:  
     ```bash  
     kubectl port-forward service/flask-service 5000:5000  
     ```  
   - Verify the app works at `localhost:5000`.  
   - Take a screenshot: `flask_k8s.png` (Flask app running via Kubernetes).  

3. **Configure Horizontal Pod Autoscaling (HPA)** (2 hours, 12:00 PM - 2:00 PM)  
   - Create `flask-hpa.yaml`: HPA to scale Flask pods based on CPU usage (target: 50%).  
     ```yaml  
     apiVersion: autoscaling/v1  
     kind: HorizontalPodAutoscaler  
     metadata:  
       name: flask-hpa  
     spec:  
       scaleTargetRef:  
         apiVersion: apps/v1  
         kind: Deployment  
         name: flask-deployment  
       minReplicas: 2  
       maxReplicas: 5  
       targetCPUUtilizationPercentage: 50  
     ```  
   - Apply:  
     ```bash  
     kubectl apply -f flask-hpa.yaml  
     ```  
   - Simulate load (e.g., using `ab` or `curl` in a loop) to test scaling.  
   - Verify scaling:  
     ```bash  
     kubectl get hpa flask-hpa -w  
     kubectl get pods  
     ```  
   - Take a screenshot: `hpa_scaling.png` (HPA metrics and pod scaling).  

**Deliverables**  
- `Dockerfile`, `flask-deployment.yaml`, `flask-service.yaml`, `flask-hpa.yaml`.  
- Screenshots: `flask_k8s.png`, `hpa_scaling.png`.  

---

## Day 3: 28/05/2025  
**Focus**: StatefulSet for PostgreSQL and Logging/Monitoring  
**Total Time**: ~5 hours (9:00 AM - 2:00 PM)

### Tasks  
1. **Configure StatefulSet for PostgreSQL** (2.5 hours, 9:00 AM - 11:30 AM)  
   - Create a PersistentVolumeClaim (PVC) for PostgreSQL data persistence.  
   - Create `postgres-statefulset.yaml`:  
     - Use image `postgres:16`.  
     - Set environment variables: `POSTGRES_DB=healthcare`, `POSTGRES_USER=postgres`, `POSTGRES_PASSWORD=secure123`.  
     - Mount PVC for `/var/lib/postgresql/data`.  
   - Create `postgres-service.yaml`: Headless Service for StatefulSet.  
   - Apply:  
     ```bash  
     kubectl apply -f postgres-statefulset.yaml  
     kubectl apply -f postgres-service.yaml  
     ```  
   - Verify PostgreSQL pod is running and data persists after pod restart.  
   - Connect Flask to StatefulSet PostgreSQL (update `app.py` with new connection string).  
   - Test API endpoints again to ensure connectivity.  
   - Take a screenshot: `postgres_statefulset.png` (StatefulSet pod and database connection).  

2. **Set Up Logging and Monitoring** (2.5 hours, 11:30 AM - 2:00 PM)  
   - Install Kubernetes Dashboard:  
     ```bash  
     kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml  
     kubectl proxy  
     ```  
     - Access Dashboard at `http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`.  
     - Create a token to log in:  
       ```bash  
       kubectl -n kubernetes-dashboard create token admin-user  
       ```  
   - Monitor Flask pods and HPA (CPU usage, replicas).  
   - Take a screenshot: `dashboard_metrics.png` (Dashboard showing Flask pods and metrics).  
   - (Optional) Explore Prometheus setup if time permits: Follow Kubernetes documentation for Prometheus Operator.  

**Deliverables**  
- `postgres-statefulset.yaml`, `postgres-service.yaml`.  
- Updated `app.py` with new PostgreSQL connection.  
- Screenshots: `postgres_statefulset.png`, `dashboard_metrics.png`.  

---

## Day 4: 29/05/2025  
**Focus**: Testing, Optimization, and GKE Deployment Preparation  
**Total Time**: ~5 hours (9:00 AM - 2:00 PM)

### Tasks  
1. **End-to-End Testing** (2 hours, 9:00 AM - 11:00 AM)  
   - Test the entire system:  
     - Access Flask app via Service (`localhost:5000/book`).  
     - Submit a booking request (POST `/book-appointment`).  
     - Verify the appointment in PostgreSQL:  
       ```bash  
       docker exec -it <postgres-pod> psql -U postgres -d healthcare -c "SELECT * FROM appointments;"  
       ```  
     - Retrieve appointments (GET `/appointments`).  
   - Simulate load to test HPA scaling (e.g., `ab -n 1000 -c 100 http://localhost:5000/`).  
   - Take a screenshot: `e2e_test.png` (Booking form, API response, PostgreSQL data).  

2. **Optimization** (1.5 hours, 11:00 AM - 12:30 PM)  
   - Add an index to `appointments` table for faster queries:  
     ```sql  
     CREATE INDEX idx_appointment_time ON appointments (appointment_time);  
     ```  
   - Verify query performance improvement:  
     ```sql  
     EXPLAIN ANALYZE SELECT * FROM appointments WHERE appointment_time > '2025-05-01';  
     ```  
   - Set resource limits for Flask pods in `flask-deployment.yaml`:  
     ```yaml  
     resources:  
       requests:  
         cpu: "200m"  
         memory: "256Mi"  
       limits:  
         cpu: "500m"  
         memory: "512Mi"  
     ```  
   - Reapply and monitor resource usage via Kubernetes Dashboard.  
   - Take a screenshot: `optimization.png` (Query performance, resource usage).  

3. **Prepare for GKE Deployment** (1.5 hours, 12:30 PM - 2:00 PM)  
   - Set up a GKE cluster:  
     - Follow GKE documentation: https://cloud.google.com/kubernetes-engine/docs.  
     - Create a small cluster (e.g., 2 nodes, standard machine type).  
     - Configure `kubectl` to connect to GKE:  
       ```bash  
       gcloud container clusters get-credentials <cluster-name> --region <region>  
       ```  
   - Test connectivity:  
     ```bash  
     kubectl get nodes  
     ```  
   - Take a screenshot: `gke_cluster.png` (GKE cluster details).  

**Deliverables**  
- Updated `flask-deployment.yaml` with resource limits.  
- SQL script: `optimization.sql` (index creation).  
- Screenshots: `e2e_test.png`, `optimization.png`, `gke_cluster.png`.  

---

## Day 5: 30/05/2025  
**Focus**: Deploy to GKE and Finalize Artifacts  
**Total Time**: ~5 hours (9:00 AM - 2:00 PM)

### Tasks  
1. **Deploy to GKE** (3 hours, 9:00 AM - 12:00 PM)  
   - Apply all Kubernetes configurations to GKE:  
     ```bash  
     kubectl apply -f flask-deployment.yaml  
     kubectl apply -f flask-service.yaml  
     kubectl apply -f flask-hpa.yaml  
     kubectl apply -f postgres-statefulset.yaml  
     kubectl apply -f postgres-service.yaml  
     ```  
   - Port-forward to test Flask app on GKE:  
     ```bash  
     kubectl port-forward service/flask-service 5000:5000  
     ```  
   - Test end-to-end on GKE (booking, retrieving appointments).  
   - Monitor HPA scaling on GKE using Kubernetes Dashboard.  
   - Take screenshots: `gke_flask.png` (Flask app on GKE), `gke_hpa.png` (HPA on GKE).  

2. **Prepare Artifacts ZIP File** (2 hours, 12:00 PM - 2:00 PM)  
   - Create a folder `HealthcareBooking_Final_Artifacts`:  
     - Source code: `app.py`, `templates/book.html`, `static/style.css`.  
     - Dockerfile: `Dockerfile`.  
     - Kubernetes YAMLs: `flask-deployment.yaml`, `flask-service.yaml`, `flask-hpa.yaml`, `postgres-statefulset.yaml`, `postgres-service.yaml`.  
     - SQL scripts: `db_setup.sql`, `optimization.sql`.  
     - Screenshots: `flask_booking_form.png`, `api_post.png`, `api_get.png`, `flask_k8s.png`, `hpa_scaling.png`, `postgres_statefulset.png`, `dashboard_metrics.png`, `e2e_test.png`, `optimization.png`, `gke_cluster.png`, `gke_flask.png`, `gke_hpa.png`.  
   - Zip the folder: `HealthcareBooking_Final_Artifacts.zip`.  

**Deliverables**  
- Deployed system on GKE.  
- `HealthcareBooking_Final_Artifacts.zip`.  
- Screenshots: `gke_flask.png`, `gke_hpa.png`.  

---

## Day 6: 31/05/2025  
**Focus**: Create Presentation, Record Demo, and Submit  
**Total Time**: ~5 hours (9:00 AM - 2:00 PM)

### Tasks  
1. **Create Presentation Slides** (2 hours, 9:00 AM - 11:00 AM)  
   - Use PowerPoint or Google Slides.  
   - Structure (based on 7.2HD guidelines):  
     - **Slide 1**: Introduction (project overview, objectives).  
     - **Slide 2-3**: Significant Design Elements (architecture diagram, Flask, PostgreSQL, Kubernetes features).  
     - **Slide 4-5**: Major Outcomes (completed work, demo highlights).  
     - **Slide 6-7**: ULO Achievement (how the project meets ULO1-5 at an advanced level).  
       - **ULO1 Note**: Frame cloud resource explanation (Minikube/GKE comparison) for a diverse audience (technical & non-technical).  
       - **ULO3 Note**: Explicitly link GKE deployment and features (scalability, HPA) to business impacts (patient experience, cost-efficiency).  
       - **ULO4 Note**: Briefly explain how modular architecture and IaC (YAMLs) facilitate team collaboration and lifecycle management.  
     - **Slide 8**: Conclusion (summary, future improvements).  
   - Include visuals: `architecture.png`, `flask_booking_form.png`, `api_get.png`, `hpa_scaling.png`, `postgres_statefulset.png`, `dashboard_metrics.png`, `gke_flask.png`.  
   - Export slides as PDF: `presentation_slides.pdf`.  

2. **Record Presentation and Demo** (2 hours, 11:00 AM - 1:00 PM)  
   - Use Kaltura Capture (via DeakinAir) to record:  
     - Present slides (8-10 minutes).  
     - Demo (5 minutes):  
       - Access Flask app on GKE (`localhost:5000/book`).  
       - Book an appointment (POST `/book-appointment`).  
       - Retrieve appointments (GET `/appointments`).  
       - Show HPA scaling (simulate load, very visually demonstrate `kubectl get hpa` and `kubectl get pods` before, during, and after load).  
       - Show Kubernetes Dashboard (metrics for Flask pods).  
       - (Optional, if smooth) Briefly demo PostgreSQL data persistence with StatefulSet after a pod restart.  
   - Total: ~15 minutes (max allowed by 7.2HD).  
   - Upload to DeakinAir (set to unlisted/public).  
   - Get the link: `presentation_link.txt`.  

3. **Prepare Submission Document** (1 hour, 1:00 PM - 2:00 PM)  
   - Create `submission_doc.pdf` (1 page):  
     - **Link to Presentation**: Include DeakinAir link from `presentation_link.txt`.  
     - **ZIP File Outline**:  
       - `app.py`, `templates/book.html`, `static/style.css`: Flask app source code.  
       - `Dockerfile`: Containerization configuration.  
       - `flask-deployment.yaml`, `flask-service.yaml`, `flask-hpa.yaml`: Flask Kubernetes configs.  
       - `postgres-statefulset.yaml`, `postgres-service.yaml`: PostgreSQL Kubernetes configs.  
       - `db_setup.sql`, `optimization.sql`: Database setup and optimization scripts.  
       - Screenshots: List all screenshots and their relevance (e.g., `flask_booking_form.png` shows UI, `hpa_scaling.png` shows scalability).  
         - **Note**: For each key artifact (especially YAMLs like `flask-hpa.yaml`, `postgres-statefulset.yaml`, and critical screenshots), explicitly map it to how it demonstrates an "Advanced" aspect of the rubric or a specific ULO.  

4. **Submit Task** (by 2:00 PM)  
   - Upload presentation to DeakinAir.  
   - Upload `HealthcareBooking_Final_Artifacts.zip` to CloudDeakin.  
   - Submit `submission_doc.pdf` to OnTrack.  

**Deliverables**  
- `presentation_slides.pdf`.  
- Recorded presentation on DeakinAir (`presentation_link.txt`).  
- `submission_doc.pdf`.  

---

## Key Notes  
- **Prioritize Kubernetes Features**: StatefulSet, HPA, and monitoring are critical for Advanced level.  
- **Demo Focus**: Highlight Kubernetes functionality (HPA scaling, StatefulSet persistence, metrics). Ensure HPA demo is very visual. Consider briefly showing StatefulSet data persistence.  
- **Presentation Focus**: Clearly articulate ULO achievement, linking technical choices to business impacts and collaborative aspects. Frame ULO1 for a diverse audience.
- **Time Management**: Stick to the schedule to avoid last-minute issues.  
- **Backup Plan**: If GKE deployment fails due to cost, use Docker Desktop for the demo, but explain the GKE plan in the presentation.  
- **Artifacts**: Ensure all files are included in the ZIP and clearly outlined in `submission_doc.pdf`, explicitly linking key artifacts to "Advanced" criteria and ULOs.  

---

**Good Luck!** With this plan, you'll achieve Advanced level for Task 7.2HD.