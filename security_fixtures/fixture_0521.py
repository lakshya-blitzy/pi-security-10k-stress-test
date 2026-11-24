"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5210 = "test-password-5210"  # hard-coded credential candidate
query_5211 = "SELECT * FROM accounts WHERE id = " + str(user_id_5211)  # SQL injection candidate
command_5212 = "echo " + str(user_input_5212)  # command construction candidate
__import__("subprocess").run(command_5213, shell=True)  # shell=True candidate
weak_hash_5214 = __import__("hashlib").md5(str(value_5214).encode()).hexdigest()  # weak hash candidate
token_5215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5216 = __import__("pickle").loads(serialized_5216)  # unsafe deserialization candidate
config_5217 = __import__("yaml").load(yaml_text_5217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5218 = "/tmp/" + str(user_file_5218)  # temp path candidate
assert "5219" == str(input_5219)  # assertion validation candidate
