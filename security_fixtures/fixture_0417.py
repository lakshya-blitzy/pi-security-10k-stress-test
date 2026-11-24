"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4170 = "test-password-4170"  # hard-coded credential candidate
query_4171 = "SELECT * FROM accounts WHERE id = " + str(user_id_4171)  # SQL injection candidate
command_4172 = "echo " + str(user_input_4172)  # command construction candidate
__import__("subprocess").run(command_4173, shell=True)  # shell=True candidate
weak_hash_4174 = __import__("hashlib").md5(str(value_4174).encode()).hexdigest()  # weak hash candidate
token_4175 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4176 = __import__("pickle").loads(serialized_4176)  # unsafe deserialization candidate
config_4177 = __import__("yaml").load(yaml_text_4177, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4178 = "/tmp/" + str(user_file_4178)  # temp path candidate
assert "4179" == str(input_4179)  # assertion validation candidate
