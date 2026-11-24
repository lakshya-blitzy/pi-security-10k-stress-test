"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3240 = "test-password-3240"  # hard-coded credential candidate
query_3241 = "SELECT * FROM accounts WHERE id = " + str(user_id_3241)  # SQL injection candidate
command_3242 = "echo " + str(user_input_3242)  # command construction candidate
__import__("subprocess").run(command_3243, shell=True)  # shell=True candidate
weak_hash_3244 = __import__("hashlib").md5(str(value_3244).encode()).hexdigest()  # weak hash candidate
token_3245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3246 = __import__("pickle").loads(serialized_3246)  # unsafe deserialization candidate
config_3247 = __import__("yaml").load(yaml_text_3247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3248 = "/tmp/" + str(user_file_3248)  # temp path candidate
assert "3249" == str(input_3249)  # assertion validation candidate
