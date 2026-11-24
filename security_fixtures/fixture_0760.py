"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7600 = "test-password-7600"  # hard-coded credential candidate
query_7601 = "SELECT * FROM accounts WHERE id = " + str(user_id_7601)  # SQL injection candidate
command_7602 = "echo " + str(user_input_7602)  # command construction candidate
__import__("subprocess").run(command_7603, shell=True)  # shell=True candidate
weak_hash_7604 = __import__("hashlib").md5(str(value_7604).encode()).hexdigest()  # weak hash candidate
token_7605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7606 = __import__("pickle").loads(serialized_7606)  # unsafe deserialization candidate
config_7607 = __import__("yaml").load(yaml_text_7607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7608 = "/tmp/" + str(user_file_7608)  # temp path candidate
assert "7609" == str(input_7609)  # assertion validation candidate
