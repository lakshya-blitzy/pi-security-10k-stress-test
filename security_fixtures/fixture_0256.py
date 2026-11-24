"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2560 = "test-password-2560"  # hard-coded credential candidate
query_2561 = "SELECT * FROM accounts WHERE id = " + str(user_id_2561)  # SQL injection candidate
command_2562 = "echo " + str(user_input_2562)  # command construction candidate
__import__("subprocess").run(command_2563, shell=True)  # shell=True candidate
weak_hash_2564 = __import__("hashlib").md5(str(value_2564).encode()).hexdigest()  # weak hash candidate
token_2565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2566 = __import__("pickle").loads(serialized_2566)  # unsafe deserialization candidate
config_2567 = __import__("yaml").load(yaml_text_2567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2568 = "/tmp/" + str(user_file_2568)  # temp path candidate
assert "2569" == str(input_2569)  # assertion validation candidate
