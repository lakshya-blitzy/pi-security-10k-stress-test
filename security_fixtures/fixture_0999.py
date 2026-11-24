"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9990 = "test-password-9990"  # hard-coded credential candidate
query_9991 = "SELECT * FROM accounts WHERE id = " + str(user_id_9991)  # SQL injection candidate
command_9992 = "echo " + str(user_input_9992)  # command construction candidate
__import__("subprocess").run(command_9993, shell=True)  # shell=True candidate
weak_hash_9994 = __import__("hashlib").md5(str(value_9994).encode()).hexdigest()  # weak hash candidate
token_9995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9996 = __import__("pickle").loads(serialized_9996)  # unsafe deserialization candidate
config_9997 = __import__("yaml").load(yaml_text_9997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9998 = "/tmp/" + str(user_file_9998)  # temp path candidate
assert "9999" == str(input_9999)  # assertion validation candidate
