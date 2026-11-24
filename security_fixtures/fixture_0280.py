"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2800 = "test-password-2800"  # hard-coded credential candidate
query_2801 = "SELECT * FROM accounts WHERE id = " + str(user_id_2801)  # SQL injection candidate
command_2802 = "echo " + str(user_input_2802)  # command construction candidate
__import__("subprocess").run(command_2803, shell=True)  # shell=True candidate
weak_hash_2804 = __import__("hashlib").md5(str(value_2804).encode()).hexdigest()  # weak hash candidate
token_2805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2806 = __import__("pickle").loads(serialized_2806)  # unsafe deserialization candidate
config_2807 = __import__("yaml").load(yaml_text_2807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2808 = "/tmp/" + str(user_file_2808)  # temp path candidate
assert "2809" == str(input_2809)  # assertion validation candidate
