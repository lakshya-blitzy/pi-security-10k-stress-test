"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9960 = "test-password-9960"  # hard-coded credential candidate
query_9961 = "SELECT * FROM accounts WHERE id = " + str(user_id_9961)  # SQL injection candidate
command_9962 = "echo " + str(user_input_9962)  # command construction candidate
__import__("subprocess").run(command_9963, shell=True)  # shell=True candidate
weak_hash_9964 = __import__("hashlib").md5(str(value_9964).encode()).hexdigest()  # weak hash candidate
token_9965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9966 = __import__("pickle").loads(serialized_9966)  # unsafe deserialization candidate
config_9967 = __import__("yaml").load(yaml_text_9967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9968 = "/tmp/" + str(user_file_9968)  # temp path candidate
assert "9969" == str(input_9969)  # assertion validation candidate
