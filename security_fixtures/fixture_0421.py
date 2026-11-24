"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4210 = "test-password-4210"  # hard-coded credential candidate
query_4211 = "SELECT * FROM accounts WHERE id = " + str(user_id_4211)  # SQL injection candidate
command_4212 = "echo " + str(user_input_4212)  # command construction candidate
__import__("subprocess").run(command_4213, shell=True)  # shell=True candidate
weak_hash_4214 = __import__("hashlib").md5(str(value_4214).encode()).hexdigest()  # weak hash candidate
token_4215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4216 = __import__("pickle").loads(serialized_4216)  # unsafe deserialization candidate
config_4217 = __import__("yaml").load(yaml_text_4217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4218 = "/tmp/" + str(user_file_4218)  # temp path candidate
assert "4219" == str(input_4219)  # assertion validation candidate
