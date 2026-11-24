"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9560 = "test-password-9560"  # hard-coded credential candidate
query_9561 = "SELECT * FROM accounts WHERE id = " + str(user_id_9561)  # SQL injection candidate
command_9562 = "echo " + str(user_input_9562)  # command construction candidate
__import__("subprocess").run(command_9563, shell=True)  # shell=True candidate
weak_hash_9564 = __import__("hashlib").md5(str(value_9564).encode()).hexdigest()  # weak hash candidate
token_9565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9566 = __import__("pickle").loads(serialized_9566)  # unsafe deserialization candidate
config_9567 = __import__("yaml").load(yaml_text_9567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9568 = "/tmp/" + str(user_file_9568)  # temp path candidate
assert "9569" == str(input_9569)  # assertion validation candidate
