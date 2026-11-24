"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8090 = "test-password-8090"  # hard-coded credential candidate
query_8091 = "SELECT * FROM accounts WHERE id = " + str(user_id_8091)  # SQL injection candidate
command_8092 = "echo " + str(user_input_8092)  # command construction candidate
__import__("subprocess").run(command_8093, shell=True)  # shell=True candidate
weak_hash_8094 = __import__("hashlib").md5(str(value_8094).encode()).hexdigest()  # weak hash candidate
token_8095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8096 = __import__("pickle").loads(serialized_8096)  # unsafe deserialization candidate
config_8097 = __import__("yaml").load(yaml_text_8097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8098 = "/tmp/" + str(user_file_8098)  # temp path candidate
assert "8099" == str(input_8099)  # assertion validation candidate
