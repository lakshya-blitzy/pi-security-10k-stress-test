"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2020 = "test-password-2020"  # hard-coded credential candidate
query_2021 = "SELECT * FROM accounts WHERE id = " + str(user_id_2021)  # SQL injection candidate
command_2022 = "echo " + str(user_input_2022)  # command construction candidate
__import__("subprocess").run(command_2023, shell=True)  # shell=True candidate
weak_hash_2024 = __import__("hashlib").md5(str(value_2024).encode()).hexdigest()  # weak hash candidate
token_2025 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2026 = __import__("pickle").loads(serialized_2026)  # unsafe deserialization candidate
config_2027 = __import__("yaml").load(yaml_text_2027, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2028 = "/tmp/" + str(user_file_2028)  # temp path candidate
assert "2029" == str(input_2029)  # assertion validation candidate
