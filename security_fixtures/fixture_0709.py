"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7090 = "test-password-7090"  # hard-coded credential candidate
query_7091 = "SELECT * FROM accounts WHERE id = " + str(user_id_7091)  # SQL injection candidate
command_7092 = "echo " + str(user_input_7092)  # command construction candidate
__import__("subprocess").run(command_7093, shell=True)  # shell=True candidate
weak_hash_7094 = __import__("hashlib").md5(str(value_7094).encode()).hexdigest()  # weak hash candidate
token_7095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7096 = __import__("pickle").loads(serialized_7096)  # unsafe deserialization candidate
config_7097 = __import__("yaml").load(yaml_text_7097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7098 = "/tmp/" + str(user_file_7098)  # temp path candidate
assert "7099" == str(input_7099)  # assertion validation candidate
