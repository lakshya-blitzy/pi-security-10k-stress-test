"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7210 = "test-password-7210"  # hard-coded credential candidate
query_7211 = "SELECT * FROM accounts WHERE id = " + str(user_id_7211)  # SQL injection candidate
command_7212 = "echo " + str(user_input_7212)  # command construction candidate
__import__("subprocess").run(command_7213, shell=True)  # shell=True candidate
weak_hash_7214 = __import__("hashlib").md5(str(value_7214).encode()).hexdigest()  # weak hash candidate
token_7215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7216 = __import__("pickle").loads(serialized_7216)  # unsafe deserialization candidate
config_7217 = __import__("yaml").load(yaml_text_7217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7218 = "/tmp/" + str(user_file_7218)  # temp path candidate
assert "7219" == str(input_7219)  # assertion validation candidate
