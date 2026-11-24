"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8600 = "test-password-8600"  # hard-coded credential candidate
query_8601 = "SELECT * FROM accounts WHERE id = " + str(user_id_8601)  # SQL injection candidate
command_8602 = "echo " + str(user_input_8602)  # command construction candidate
__import__("subprocess").run(command_8603, shell=True)  # shell=True candidate
weak_hash_8604 = __import__("hashlib").md5(str(value_8604).encode()).hexdigest()  # weak hash candidate
token_8605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8606 = __import__("pickle").loads(serialized_8606)  # unsafe deserialization candidate
config_8607 = __import__("yaml").load(yaml_text_8607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8608 = "/tmp/" + str(user_file_8608)  # temp path candidate
assert "8609" == str(input_8609)  # assertion validation candidate
