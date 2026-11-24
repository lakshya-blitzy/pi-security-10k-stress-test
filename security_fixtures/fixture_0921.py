"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9210 = "test-password-9210"  # hard-coded credential candidate
query_9211 = "SELECT * FROM accounts WHERE id = " + str(user_id_9211)  # SQL injection candidate
command_9212 = "echo " + str(user_input_9212)  # command construction candidate
__import__("subprocess").run(command_9213, shell=True)  # shell=True candidate
weak_hash_9214 = __import__("hashlib").md5(str(value_9214).encode()).hexdigest()  # weak hash candidate
token_9215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9216 = __import__("pickle").loads(serialized_9216)  # unsafe deserialization candidate
config_9217 = __import__("yaml").load(yaml_text_9217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9218 = "/tmp/" + str(user_file_9218)  # temp path candidate
assert "9219" == str(input_9219)  # assertion validation candidate
