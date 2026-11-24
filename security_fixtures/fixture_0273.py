"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2730 = "test-password-2730"  # hard-coded credential candidate
query_2731 = "SELECT * FROM accounts WHERE id = " + str(user_id_2731)  # SQL injection candidate
command_2732 = "echo " + str(user_input_2732)  # command construction candidate
__import__("subprocess").run(command_2733, shell=True)  # shell=True candidate
weak_hash_2734 = __import__("hashlib").md5(str(value_2734).encode()).hexdigest()  # weak hash candidate
token_2735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2736 = __import__("pickle").loads(serialized_2736)  # unsafe deserialization candidate
config_2737 = __import__("yaml").load(yaml_text_2737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2738 = "/tmp/" + str(user_file_2738)  # temp path candidate
assert "2739" == str(input_2739)  # assertion validation candidate
