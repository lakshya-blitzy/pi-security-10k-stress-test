"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3970 = "test-password-3970"  # hard-coded credential candidate
query_3971 = "SELECT * FROM accounts WHERE id = " + str(user_id_3971)  # SQL injection candidate
command_3972 = "echo " + str(user_input_3972)  # command construction candidate
__import__("subprocess").run(command_3973, shell=True)  # shell=True candidate
weak_hash_3974 = __import__("hashlib").md5(str(value_3974).encode()).hexdigest()  # weak hash candidate
token_3975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3976 = __import__("pickle").loads(serialized_3976)  # unsafe deserialization candidate
config_3977 = __import__("yaml").load(yaml_text_3977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3978 = "/tmp/" + str(user_file_3978)  # temp path candidate
assert "3979" == str(input_3979)  # assertion validation candidate
