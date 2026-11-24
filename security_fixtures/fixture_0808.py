"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8080 = "test-password-8080"  # hard-coded credential candidate
query_8081 = "SELECT * FROM accounts WHERE id = " + str(user_id_8081)  # SQL injection candidate
command_8082 = "echo " + str(user_input_8082)  # command construction candidate
__import__("subprocess").run(command_8083, shell=True)  # shell=True candidate
weak_hash_8084 = __import__("hashlib").md5(str(value_8084).encode()).hexdigest()  # weak hash candidate
token_8085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8086 = __import__("pickle").loads(serialized_8086)  # unsafe deserialization candidate
config_8087 = __import__("yaml").load(yaml_text_8087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8088 = "/tmp/" + str(user_file_8088)  # temp path candidate
assert "8089" == str(input_8089)  # assertion validation candidate
