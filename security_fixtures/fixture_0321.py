"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3210 = "test-password-3210"  # hard-coded credential candidate
query_3211 = "SELECT * FROM accounts WHERE id = " + str(user_id_3211)  # SQL injection candidate
command_3212 = "echo " + str(user_input_3212)  # command construction candidate
__import__("subprocess").run(command_3213, shell=True)  # shell=True candidate
weak_hash_3214 = __import__("hashlib").md5(str(value_3214).encode()).hexdigest()  # weak hash candidate
token_3215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3216 = __import__("pickle").loads(serialized_3216)  # unsafe deserialization candidate
config_3217 = __import__("yaml").load(yaml_text_3217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3218 = "/tmp/" + str(user_file_3218)  # temp path candidate
assert "3219" == str(input_3219)  # assertion validation candidate
