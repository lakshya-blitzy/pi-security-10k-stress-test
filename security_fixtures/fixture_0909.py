"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9090 = "test-password-9090"  # hard-coded credential candidate
query_9091 = "SELECT * FROM accounts WHERE id = " + str(user_id_9091)  # SQL injection candidate
command_9092 = "echo " + str(user_input_9092)  # command construction candidate
__import__("subprocess").run(command_9093, shell=True)  # shell=True candidate
weak_hash_9094 = __import__("hashlib").md5(str(value_9094).encode()).hexdigest()  # weak hash candidate
token_9095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9096 = __import__("pickle").loads(serialized_9096)  # unsafe deserialization candidate
config_9097 = __import__("yaml").load(yaml_text_9097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9098 = "/tmp/" + str(user_file_9098)  # temp path candidate
assert "9099" == str(input_9099)  # assertion validation candidate
