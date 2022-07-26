pipeline
{ 
  agent any
  stages
  {
    stage('Test')
    {
      echo 'testing'
    }
    stage('Build Master')
    {
      when
      {
        branch 'master'
      }
      steps
      {
        echo 'Building Master'
      }
    }
    stage('Build Dev')
    {
      when
      {
        branch 'dev'
      }
      steps
      {
        echo 'Building dev'
      }
    }
  }
}
